```csharp
namespace Project.Tests.Infrastructure.Domain.Brands
{
    public class BrandRepositoryTest
    {
        private readonly MultitenantContext _context;
        private readonly BrandRepository _repository;
        private readonly MultitenantContextHelper _contextHelper;

        public BrandRepositoryTest()
        {
            _context = ContextMocked.CreateMultitenantContext();
            _repository = new BrandRepository(_context);
            _contextHelper = new MultitenantContextHelper(_context);
        }

        [Fact]
        public async Task CreateAsync_AddsBrand()
        {
            // Arrange
            var brand = EntityFaker.RandomBrand();

            // Act
            await _repository.CreateAsync(brand);
            await _context.SaveChangesAsync();
            var result = await _context.Brands.FindAsync(brand.Id);

            // Assert
            Assert.NotNull(result);
            Assert.Equal(brand.Id, result.Id);
        }

        [Fact]
        public async Task GetByIdAsync_ReturnsBrand()
        {
            // Arrange
            var brands = await _contextHelper.AddBrandsAsync();
            var brand = brands.First();

            // Act
            var result = await _repository.GetByIdAsync(brand.Id);

            // Assert
            Assert.NotNull(result);
            Assert.Equal(brand.Id, result.Id);
        }

        [Fact]
        public async Task GetAllAsync_ReturnsAllBrands()
        {
            // Arrange
            var brands = await _contextHelper.AddBrandsAsync();

            // Act
            var result = await _repository.GetAllAsync();

            // Assert
            Assert.Equal(brands.Count(), result.Results.Count);
        }

        [Fact]
        public async Task GetAllAsync_WithSkipAndTake_ReturnsPaginatedBrands()
        {
            // Arrange
            var brands = await _contextHelper.AddBrandsAsync();
            int skip = 5;
            int take = 5;

            // Act
            var result = await _repository.GetAllAsync(skip: skip, take: take);

            // Assert
            Assert.Equal(take, result.Results.Count);
            var expectedBrands = brands.Skip(skip).Take(take).ToList();
            for (int i = 0; i < expectedBrands.Count; i++)
            {
                Assert.Equal(expectedBrands[i].Id, result.Results[i].Id);
            }
        }

        [Fact]
        public async Task GetAllAsync_WithNameSpecification_ReturnsMatchingBrands()
        {
            // Arrange
            var brands = await _contextHelper.AddBrandsAsync();
            var brand = brands.First();
            var specification = new BrandIdOrNameSpecification(brand.Name);

            // Act
            var result = await _repository.GetAllAsync(specification: specification);

            // Assert
            Assert.Contains(result.Results, b => b.Name == brand.Name);
        }

        [Fact]
        public async Task GetAllAsync_WithIdSpecification_ReturnsMatchingBrands()
        {
            // Arrange
            var brands = await _contextHelper.AddBrandsAsync();
            var brand = brands.First();
            var specification = new BrandIdOrNameSpecification(brand.Id);

            // Act
            var result = await _repository.GetAllAsync(specification: specification);

            // Assert
            Assert.Contains(result.Results, b => b.Id == brand.Id);
        }

        [Fact]
        public async Task GetAllAsync_OrderByName_ReturnsOrderedBrands()
        {
            // Arrange
            var brands = await _contextHelper.AddBrandsAsync();
            var orderStrategy = new OrderByNameStrategy();

            // Act
            var result = await _repository.GetAllAsync(strategy: orderStrategy);

            // Assert
            var orderedBrands = brands.OrderBy(b => b.Name).ToList();
            for (int i = 0; i < orderedBrands.Count; i++)
            {
                Assert.Equal(orderedBrands[i].Name, result.Results[i].Name);
            }
        }

        [Fact]
        public async Task Delete_RemovesBrand()
        {
            // Arrange
            var brands = await _contextHelper.AddBrandsAsync();
            var brand = brands.First();

            // Act
            _repository.Delete(brand);
            await _context.SaveChangesAsync();
            var result = await _context.Brands.FindAsync(brand.Id);

            // Assert
            Assert.Null(result);
        }

        [Fact]
        public async Task Update_UpdatesBrand()
        {
            // Arrange
            var brands = await _contextHelper.AddBrandsAsync();
            var brand = brands.First();
            var newName = "Updated Name";

            // Act
            brand.SetName(newName);
            _repository.Update(brand);
            await _context.SaveChangesAsync();
            var result = await _context.Brands.FindAsync(brand.Id);

            // Assert
            Assert.NotNull(result);
            Assert.Equal(newName, result.Name);
        }
    }
}
```