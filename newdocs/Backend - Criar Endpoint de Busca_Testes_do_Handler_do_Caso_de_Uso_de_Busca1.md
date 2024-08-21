```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public class GetAllBrandsHandlerTest
    {
        private readonly IBrandRepository _brandRepository = Substitute.For<IBrandRepository>();
        private readonly IMapper _mapper = Substitute.For<IMapper>();
        private readonly GetAllBrandsHandler _handler;

        public GetAllBrandsHandlerTest()
        {
            _handler = new GetAllBrandsHandler(_brandRepository, _mapper);
        }

        [Fact]
        public async Task Handle_ReturnsBrands()
        {
            // Arrange
            var query = BrandHelper.RandomGetAllBrandsQuery();
            var brands = new PaginatedResponse<Brand>
            {
                TotalResults = 10,
                Results = EntityFaker.RandomBrands(10)
            };
            var dto = new PaginatedResponse<GetAllBrandsDto>
            {
                TotalResults = 10,
                Results = new List<GetAllBrandsDto>()
            };

            _brandRepository.GetAllAsync(Arg.Any<Specification<Brand>>(), Arg.Any<OrderStrategy<Brand>>(), Arg.Any<int?>(), Arg.Any<int?>())
                .Returns(brands);
            _mapper.Map<PaginatedResponse<GetAllBrandsDto>>(brands).Returns(dto);

            // Act
            var result = await _handler.Handle(query, CancellationToken.None);

            // Assert
            Assert.NotNull(result);
            Assert.Equal(dto.TotalResults, result.TotalResults);
            Assert.Equal(dto.Results, result.Results);
        }
    }
}
```