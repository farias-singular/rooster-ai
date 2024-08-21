```csharp
namespace Project.Tests.Infrastructure.Domain.Brands
{
    public class BrandUniquenessCheckerTest
    {
        private readonly MultitenantContext _context;
        private readonly BrandUniquenessChecker _uniquenessChecker;
        private readonly MultitenantContextHelper _contextHelper;

        public BrandUniquenessCheckerTest()
        {
            _context = ContextMocked.CreateMultitenantContext();
            _uniquenessChecker = new BrandUniquenessChecker(_context);
            _contextHelper = new MultitenantContextHelper(_context);
        }

        [Fact]
        public void IsUnique_ReturnsTrue_WhenBrandIsUnique()
        {
            // Arrange
            var brand = EntityFaker.RandomBrand();
            _context.Brands.Add(brand);
            _context.SaveChanges();

            // Act
            var result = _uniquenessChecker.IsUnique("new-id", brand.OrganizationId);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public void IsUnique_ReturnsFalse_WhenBrandIsNotUnique()
        {
            // Arrange
            var brand = EntityFaker.RandomBrand();
            _context.Brands.Add(brand);
            _context.SaveChanges();

            // Act
            var result = _uniquenessChecker.IsUnique(brand.Id, brand.OrganizationId);

            // Assert
            Assert.False(result);
        }

        [Fact]
        public async Task IsUniqueAsync_ReturnsTrue_WhenBrandIsUnique()
        {
            // Arrange
            var brand = EntityFaker.RandomBrand();
            await _context.Brands.AddAsync(brand);
            await _context.SaveChangesAsync();

            // Act
            var result = await _uniquenessChecker.IsUniqueAsync("new-id", brand.OrganizationId);

            // Assert
            Assert.True(result);
        }

        [Fact]
        public async Task IsUniqueAsync_ReturnsFalse_WhenBrandIsNotUnique()
        {
            // Arrange
            var brand = EntityFaker.RandomBrand();
            await _context.Brands.AddAsync(brand);
            await _context.SaveChangesAsync();

            // Act
            var result = await _uniquenessChecker.IsUniqueAsync(brand.Id, brand.OrganizationId);

            // Assert
            Assert.False(result);
        }
    }
}
```